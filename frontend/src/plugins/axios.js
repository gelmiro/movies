import Vue from 'vue'
import VueAxios from 'vue-axios'
import axios from "axios";

Vue.use(VueAxios, axios)
Vue.axios.defaults.baseURL = 'http://dev4.scout.wro.nsn-rdnet.net/api/v1/'