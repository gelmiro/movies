<template>
  <div>
    <v-app-bar color="#0D47A1" fixed app :clipped-left="$vuetify.breakpoint.lgAndUp"></v-app-bar>
    <v-main>
      <v-container fluid>

        <v-row justify="center">
          <v-card width="470">
            <v-form @submit.prevent="onLogin" ref="form">
              <v-container>
                <div style="height: 30px">
                  <v-slide-y-transition>
                    <span v-for="error in errors" class="caption red--text text-xs-center" :key="error">{{ error }}</span>
                  </v-slide-y-transition>
                </div>
                <v-text-field
                    autofocus
                    type="text"
                    v-model="username"
                    label="Username"
                    :rules="[rules.required]"
                ></v-text-field>
                <v-text-field
                    type="password"
                    v-model="password"
                    label="Password"
                    :rules="[rules.required]"
                ></v-text-field>
                <v-card-actions>
                  <v-spacer/>
                  <v-btn text :loading="loading" type="submit">Log in</v-btn>
                </v-card-actions>
              </v-container>
            </v-form>
          </v-card>
        </v-row>
      </v-container>
    </v-main>
  </div>
</template>

<script>
import _ from 'lodash'
import {mapActions} from 'vuex'

export default {

  name: "Login",
  data() {
    return {
      username: '',
      password: '',
      rules: {
        required: val => _.isNil(val) || !val.length ? 'field is required!' : true
      },

      errors: [],
      loading: false
    }
  },
  computed: {},
  methods: {
    ...mapActions(['login']),
    async onLogin() {
      this.loading = true
      try {
        await this.login({username: this.username, password: this.password})
        this.$router.push('/')
      } catch (error) {
        this.errors = _.get(error, 'response.data.non_field_errors', ['Unknown error'])
      }
      this.loading = false

    }
  },
}
</script>

<style scoped>

</style>