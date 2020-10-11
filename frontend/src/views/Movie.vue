<template>
  <div>
    <v-layout row justify-center>
      <v-flex xs3>
        <v-text-field
            autofocus
            type="text"
            v-model="search"
            :loading="loading"
            label="Search"
            placeholder="Start typing title"
            clearable
            :error-messages="errors"
        ></v-text-field>
      </v-flex>
    </v-layout>
    <v-container fluid>
      <app-movie-cards
      @triggeredMovie="updateFavourite"
      :movies-data="moviesDisplay"
      ></app-movie-cards>
      <v-container>
        <v-pagination
            v-model="page"
            class="my-4"
            :length="numberOfPages"
            :total-visible="7"
            :disabled="loading"
        ></v-pagination>
      </v-container>
    </v-container>
  </div>
</template>

<script>
import _ from 'lodash'
import {mapState, mapActions} from "vuex";
import MovieCards from "../components/MovieCards";

export default {
  name: "Movie",
  components: {
    'appMovieCards': MovieCards,
  },
  data() {
    return {
      search: '',
      loading: false,
      errors: [],
      page: 1
    }
  },
  computed: {
    ...mapState({
      movies: state => state.requests.movies,
      favouriteMovies: state => state.requests.favouriteMovies
    }),
    numberOfPages() {
      return Math.ceil(_.get(this.movies, 'meta.total_results', 1) / 100)
    },
    moviesDisplay() {
      const movies = []
      for (const movie of this.movies) {
        const favourite = _.find(this.favouriteMovies, {imdbID: movie.imdbID})
        if (favourite) {
          movies.push(Object.assign({favourite: true, id: favourite.id}, movie))
        } else {
          movies.push(movie)
        }
      }
      return movies
    }
  },
  methods: {
    ...mapActions(['searchMovie', 'addFavouriteMovie', 'getFavouriteMovie', 'removeFavouriteMovie']),
    async updateFavourite(movie) {
      if (movie.id) {
        await this.removeFavouriteMovie(movie)
      } else {
        await this.addFavouriteMovie(movie)
      }

    }
  },
  watch: {
    search: _.debounce(async function(value) {
      this.loading = true
      this.errors = []
      try {
        await this.searchMovie({text: value})
      } catch (error) {
        this.errors = _.get(error, 'response.data', [])
      }
      this.loading = false
    }, 1000),
    page: async function(value) {
      this.loading = true
      await this.searchMovie({text: this.search, page: value})
      this.loading = false
    }
  },
  created() {
    this.getFavouriteMovie()
  }
}
</script>

<style scoped>

</style>