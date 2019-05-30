import Vue from 'vue'
import Vuex from 'vuex'

import tasks from './index'

Vue.use(Vuex)

export const store = new Vuex.Store({
  modules: {
    tasks
  },


  state: {
    tasks: 'All tasks'
  },
  getters: {
    task: state => state.tasks
  },

  mutations: {

  },
  actions: {},

  strict: process.env.NODE_ENV !== 'production'

})

export default store
