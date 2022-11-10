<template>
    <div class="important" style="border:1px solid gray; border-radius: 5px 5px 5px 5px; margin:15px; padding:20px; font-size: 15px;">
      <span>
        <button v-if="todo.isCompleted" @click="check" style="background-color:rgba(0,0,0,0); border:0;"><i class="bi bi-circle-fill"></i></button>
        <button @click="check" style="background-color:rgba(0,0,0,0); border:0;" v-else><i class="bi bi-circle"></i></button>
      </span>
      {{todo.content}}
      <span style="float:right;">
        <button v-if="todo.isImportant" @click="important" style="background-color:rgba(0,0,0,0); border:0;"><i class="bi bi-star-fill"></i></button>
        <button @click="important" style="background-color:rgba(0,0,0,0); border:0;" v-else><i class="bi bi-star"></i></button>
      </span>
    </div>
</template>
  
  <script>

  export default {
    name:'ImportantTodoList',
    props: {
      todo: Object,
    },
    components: {
    },
    methods: {
      important() {
        this.$store.dispatch('important',this.todo)
      },
      check() {
        this.$store.dispatch('check',this.todo)
      }
    }
  }
  </script>
  
  <style>

  </style>