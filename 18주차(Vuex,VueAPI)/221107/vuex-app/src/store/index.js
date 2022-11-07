import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    message: '일정을 입력하세요',
    todoList : [],
  },
  getters: {
    messageLength(state) {
      return state.message.length
    }
  },
  // state 의 값을 변경하는 역할을 한다.(동기식 처리)
  mutations: {
    CHANGE_TODO(state, todo) {
      state.todoList.push(todo)
    }
  },
  // mutations 이외의 나머지 로직을 처리한다.(비동기식 처리 가능)
  actions: {
    changeTodo(context, todo) {
      context.commit('CHANGE_TODO', todo)
    }
  },
  modules: {
  }
})
