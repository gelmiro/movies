<template>
  <div>
    <v-row justify-center>
      <v-container fluid>
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