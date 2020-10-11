<template>
  <div>
    <v-row justify="center">
      <v-card width="470">
        <v-form @submit.prevent="onLogin" ref="form">
          <v-container>
            <div style="height: 30px">
              <v-slide-y-transition>
                <span v-for="error in errors.non_field_errors" class="caption red--text text-xs-center" :key="error">{{ error }}</span>
              </v-slide-y-transition>
            </div>
            <v-text-field
                autofocus
                type="text"
                v-model="user.username"
                label="Username"
                :error-messages="errors.username"
                :rules="[rules.required]"
            ></v-text-field>
            <v-text-field
                type="password"
                v-model="user.password"
                label="password"
                :error-messages="errors.password"
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
  </div>
</template>

<script>
import _ from 'lodash'
import {mapActions} from 'vuex'

export default {

  name: "Login",
  data() {
    const blankErrors = Object.freeze({
      username: [],
      password: [],
      non_field_errors: []
    })
    return {
      user: {
        username: '',
        password: '',
      },

      rules: {
        required: val => _.isNil(val) || !val.length ? 'field is required!' : true
      },

      errors: Object.assign({}, blankErrors),
      blankErrors,
      loading: false
    }
  },
  computed: {},
  methods: {
    ...mapActions(['login']),
    async onLogin() {
      this.loading = true
      this.errors = Object.assign({}, this.blankErrors)
      try {
        await this.login(this.user)
        this.$router.push('/')
      } catch (error) {
        Object.assign(this.errors, error.response.data)
      }
      this.loading = false

    }
  },
}
</script>

<style scoped>

</style>