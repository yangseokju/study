import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    counter:0,
  },
  getters: {
    counterdouble(state) {
      return state.counter * 2
    }
  },
  mutations: {
    INCREASE(state) {
      state.counter += 1
      console.log(state.counter)
    },
    DECREASE(state) {
      state.counter -= 1
      console.log(state.counter)
    },
  },
  actions: {
    increase(context) {
      context.commit('INCREASE')
    },
    decrease(context) {
      context.commit('DECREASE')
    }
  },
  modules: {
  }
})
