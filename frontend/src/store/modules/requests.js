import Vue from "vue";

const state = {
  movies: [],
  favouriteMovies: []
}

const getters = {}

const mutations = {
  setMovies(state, payload) {
    let movies = payload.data
    movies.meta = payload.meta
    state.movies = movies
  },
    clearMovies(state) {
    state.movies = []
  },
  setFavouriteMovies(state, payload) {
    state.favouriteMovies = payload
  }
}

const actions = {
  async searchMovie({commit, rootState}, {text, page = 1}) {
     commit('clearMovies')
    const response = await Vue.axios.get('/movies/omdb/', {
      params: {s: text, page},
      headers: {'Authorization': `JWT ${rootState.authentication.token}`}
    })
    commit('setMovies', response.data)
    return response
  },
  async addFavouriteMovie({rootState, dispatch}, {users, imdbID, Title, Year, Type, Poster}) {
    const response = await Vue.axios.post('/movies/',
      {users, imdbID, Title, Year, Type, Poster},
      {
        headers: {'Authorization': `JWT ${rootState.authentication.token}`}
      })
    await dispatch('getFavouriteMovie')
    return response
  },
  async removeFavouriteMovie({rootState, dispatch}, {id}) {
    console.log('id', id)
    const response = await Vue.axios.delete(`/movies/${id}/`,
      {
        headers: {'Authorization': `JWT ${rootState.authentication.token}`}
      })
    await dispatch('getFavouriteMovie')
    return response
  },
  async getFavouriteMovie({commit, rootState}) {
    const response = await Vue.axios.get('/movies/',
      {
        headers: {'Authorization': `JWT ${rootState.authentication.token}`}
      })
    commit('setFavouriteMovies', response.data)
    return response
  }
}


export default {
  state,
  getters,
  mutations,
  actions
}

