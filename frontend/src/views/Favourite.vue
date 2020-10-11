<template>
  <div>
    <v-row justify-center>
      <v-container fluid>
        <v-alert
            v-model="show"
            type="info"
            outlined
        >
          You do not have favourites movies yet. Go to <router-link to="/movies">search</router-link> and add something.
        </v-alert>
        <app-movie-cards
            @triggeredMovie="removeFavourite"
            :movies-data="moviesDisplay"
        ></app-movie-cards>
      </v-container>
    </v-row>
  </div>
</template>

<script>
import {mapState, mapActions} from "vuex";
import MovieCards from "../components/MovieCards";

export default {
  name: "Favourites",
  components: {
    'appMovieCards': MovieCards,
  },
  data() {
    return {}
  },
  computed: {
    ...mapState({
      favouriteMovies: state => state.requests.favouriteMovies
    }),
    moviesDisplay() {
      const movies = []
      for (const movie of this.favouriteMovies) {
        movies.push(Object.assign({favourite: true}, movie))
      }
      return movies
    },
    show() {
      return this.moviesDisplay.length === 0
    }
  },
  methods: {
    ...mapActions(['getFavouriteMovie', 'removeFavouriteMovie']),
    async removeFavourite(movie) {
      await this.removeFavouriteMovie(movie)
    }
  },
  watch: {},
  created() {
    this.getFavouriteMovie()
  }
}
</script>

<style scoped>

</style>