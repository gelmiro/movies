import Vue from 'vue'
import jwt_decode from 'jwt-decode'
import router from "../../router";

const token = localStorage.getItem('token')
const {username, email, exp} = jwt_decode(token)
Vue.axios.defaults.headers = {'Authorization': `JWT ${localStorage.getItem('token')}`}

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
  setToken(state, token) {
    state.token = token
    localStorage.setItem('token', token)
    Vue.axios.defaults.headers = {'Authorization': `JWT ${localStorage.getItem('token')}`}
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
    try {
      await Vue.axios.post('/register/', {
        username,
        first_name: firstName,
        last_name: lastName,
        email,
        password
      })
      router.push({name: 'login'})
    } catch (error) {
      return error
    }

  }
}

export default {
  state,
  getters,
  mutations,
  actions
}

