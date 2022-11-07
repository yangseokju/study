<template>
  <div id="app">
    <h1> {{message}}</h1>
    <!-- <h2>입력된 문자의 길이는 : {{messageLength}}</h2> -->
    <input 
    type="text"
    @keyup.enter = "changeTodo"
    v-model = "inputData"
    >
    <ul v-for="(todo, index) in todoList" :key="index">
      <li>{{todo}} / 입력된 문자의 길이는 : {{todo.length}}</li>
    </ul>
  </div>
</template>

<script>

export default {
  name: 'App',
  components: {
  },
  data() {
    return {
      inputData : null
    }
  },
  computed: {
    message() {
      return this.$store.state.message
    },
    todoList() {
      return this.$store.state.todoList
    }
    // messageLength() {
    //   return this.$store.getters.messageLength
    // },
    // todoList() {
    //   this.$store.state.todoList.forEach((todo) => {
    //     return todo
    //   });
    // }
  },
  methods: {
    changeTodo() {
      const newTodo = this.inputData
      this.$store.dispatch('changeTodo', newTodo)
      this.inputData = null
    },
  }
}
</script>

<style>
/* #app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
} */
</style>
