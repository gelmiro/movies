import Vue from 'vue'
import jwt_decode from 'jwt-decode'

const token = localStorage.getItem('token')
let decoded
try {
  decoded = jwt_decode(token)

} catch {
  decoded = {}
}
const {username, email, exp} = decoded


const state = {
  token,
  user: {
    username,
    email,
    exp
  }
}

const getters = {}

const mutations = {
  setUser(state, {username, email, exp}) {
    state.user.username = username
    state.user.email = email
    state.user.exp = exp
  },
  logout(state) {
    localStorage.removeItem('token')
    state.token = null
    state.user.username = null
    state.user.email = null
    state.user.exp = null
  },
  setToken(state, token) {
    state.token = token
    localStorage.setItem('token', token)
  }
}

const actions = {
  async login({commit}, {username, password}) {
    const response = await Vue.axios.post('/api_token_obtain/', {username, password})
    commit('setToken', response.data.token)
    commit('setUser', jwt_decode(response.data.token))
    return response
  },
  async register(_, {username, firstName, lastName, email, password}) {

    return await Vue.axios.post('/register/', {
      username,
      first_name: firstName,
      last_name: lastName,
      email,
      password
    })
  }
}

export default {
  state,
  getters,
  mutations,
  actions
}

