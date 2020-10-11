<template>
  <div>
    <v-container fluid>
      <v-row dense>
        <v-col
            v-for="movie in moviesData"
            :key="movie.imdbID"
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
                <v-icon
                    :color="movie.favourite ? 'red'  : 'blue'"
                    @click="updateFavourite(movie)"
                >mdi-heart
                </v-icon>
              </v-btn>

            </v-card-actions>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>

export default {
  name: "Movies",
  props: {
    moviesData: Array
  },
  data() {
    return {}
  },
  computed: {},
  methods: {
    updateFavourite(movie) {
      this.$emit('triggeredMovie', movie)
    }
  },
  watch: {}
}
</script>

<style scoped>

</style>