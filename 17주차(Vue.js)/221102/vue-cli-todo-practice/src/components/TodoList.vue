<template>
    <div>
      <ul v-for="(todo, index) in todos" :key="index">
        <TodoListItem :todo="todo" @delete-todo="deleteTodo"/>
      </ul>
    </div>
</template>

<script>
import TodoListItem from '@/components/TodoListItem'
export default {
    name:'TodoList',
    components: {
    TodoListItem,
  },
  // 상위로부터 받을때 사용
  props: {
    todos: Array,
  },
  methods: {
    deleteTodo: function(todo) {
        this.$emit('delete-todo', todo)
    }
  }
}

</script>

<style>

</style>