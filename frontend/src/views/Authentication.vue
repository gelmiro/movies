<template>
  <div>
    <v-app-bar color="#0D47A1" fixed app dark>
      <v-toolbar-title>
        <h2>My Movies</h2>
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn icon to="/register">
        <v-icon>mdi-account-plus</v-icon>
      </v-btn>
      <v-btn icon to="/login">
        <v-icon>mdi-account-check</v-icon>
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

export default {
  name: "Authentication",
}
</script>

<style scoped>

</style>