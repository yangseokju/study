import Vue from 'vue'
import Vuex from 'vuex'
import todo from './modules/todo.js'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
  },
  getters: {
  },
  mutations: {
    IMPORTANT(state,todo) {
      if (todo.isImportant) {
        todo.isImportant =false
      } else if (todo.isImportant === false) {
        todo.isImportant = true
      }
    },
    ADDPLAN(state, addplan) {
      state.todo.list.push(addplan)
    },
    CHECK(state,todo) {
      if (todo.isCompleted) {
        todo.isCompleted =false
      } else if (todo.isCompleted === false) {
        todo.isCompleted = true
      }
    }
  },
  actions: {
    important(context, todo) {
      context.commit('IMPORTANT', todo)
    },
    addplan(context, adddata) {
      const date = new Date()
      const year = date.getFullYear()
      const month = date.getMonth()
      const day = date.getDate()
      const addplan = {
          id: date.getTime(),
          content: adddata,
          dueDateTime: `${year}-${month + 1}-${day + 1}T00:00`,
          isCompleted: false,
          isImportant: false,
        }
      context.commit('ADDPLAN', addplan)
    },
    check(context,todo) {
      context.commit('CHECK', todo)
    }
  },
  modules: {
    todo,
  }
})