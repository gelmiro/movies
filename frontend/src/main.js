import Vue from 'vue'
import vuetify from './plugins/vuetify'
import App from './App'
import './plugins/axios'
import router from './router'

import store from './store'
Vue.config.productionTip = false


new Vue({
  el: '#app',
  vuetify,
  router,
  store,
  render: h => h(App),
}).$mount('#app')