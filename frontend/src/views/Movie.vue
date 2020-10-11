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
            clearable
            :error-messages="errors"
        ></v-text-field>
      </v-flex>
    </v-layout>
    <v-container fluid>
      <v-row dense>
        <v-col
            v-for="movie in movies"
            :key="movie.Title"
            :cols="2"
        >
          <v-card>
            <v-img
                :src="movie.Poster"
                class="white--text align-end"
                gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
                height="400px"
            >
              <v-card-title v-text="movie.Title"></v-card-title>
            </v-img>

            <v-card-actions>
              <v-spacer></v-spacer>

              <v-btn icon>
                <v-icon>mdi-heart</v-icon>
              </v-btn>

            </v-card-actions>
          </v-card>
        </v-col>
      </v-row>
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

export default {
  name: "Movie",
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
      movies: state => state.requests.movies
    }),
    numberOfPages() {
      return Math.ceil(_.get(this.movies, 'meta.total_results', 1) / 100)
    }
  },
  methods: {
    ...mapActions(['searchMovie']),
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
  }
}
</script>

<style scoped>

</style>