<template>
  <div>
    <v-app-bar color="#0D47A1" fixed app dark>
      <v-toolbar-title>
        <h2>My Movies</h2>
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn icon to="/movies">
        <v-icon>mdi-movie-search</v-icon>
      </v-btn>
      <v-btn icon to="/favourites">
        <v-icon>mdi-heart</v-icon>
      </v-btn>
      <v-btn icon @click="bye">
        <v-icon>mdi-logout</v-icon>
      </v-btn>
    </v-app-bar>
    <v-main>
      <v-container fluid>
        <router-view/>
      </v-container>
    </v-main>
  </div>
</template>

<script>
import {mapMutations} from 'vuex'

export default {
  name: "Home",
  methods: {
    ...mapMutations(['logout']),
    bye() {
      this.logout()
      this.$router.push('/login')
    }
  }

}
</script>

<style scoped>

</style>