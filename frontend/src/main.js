import Vue from 'vue'
import vuetify from './plugins/vuetify'
import App from './App'
import router from './router'
import axios from 'axios'
import VueAxios from 'vue-axios'
Vue.config.productionTip = false

Vue.use(VueAxios, axios)

new Vue({
  el: '#app',
  vuetify,
  router,
  render: h => h(App),
}).$mount('#app')
