import Vue from "vue";

const state = {
  movies: [],
}

const getters = {}

const mutations = {
  setMovies(state, payload) {
    let movies = payload.data
    movies.meta = payload.meta
    state.movies = movies

  }
}

const actions = {
  async searchMovie({commit, rootState}, {text, page = 1}) {
    const response = await Vue.axios.get('/movies/omdb/', {
      params: {s: text, page},
      headers: {'Authorization': `JWT ${rootState.authentication.token}`}
    })
    commit('setMovies', response.data)
    return response
  },
}


export default {
  state,
  getters,
  mutations,
  actions
}

