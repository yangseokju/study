<template>
    <div class="alltodopage">
        <div style="margin:20px">
            <h1>모든 할일</h1>
            <div class="input-group mb-3">
              <button @click="addplan" class="btn btn-outline-secondary" type="button" id="button-addon1">+</button>
              <input @keyup.enter="addplan" type="text" class="form-control" placeholder="" aria-label="Example text with button addon" aria-describedby="button-addon1" v-model="adddata">
            </div>
            <hr>
        </div>
        <div>
            <ImportantTodoPage
            v-for="(todo, index) in todoList"
            :key="index+'i'"
            :todo="todo"
            />
        </div>
            <!-- <ImportantTodoPage
            v-for="(todo, index) in importanttodoList"
            :key="index+'i'"
            :todo="todo"
            /> -->
        <!-- <div v-for="(nimportant, index) in nimportanttodoList" :key="index+'ni'" style="border:1px solid gray; border-radius: 5px 5px 5px 5px; margin:15px; padding:20px; font-size: 15px;">
          <button style="background-color:rgba(0,0,0,0); border:0;"><i class="bi bi-circle"></i></button>
          {{nimportant.content}}
          <span style="float:right;">
            <button @click="important(nimportant)" style="background-color:rgba(0,0,0,0); border:0;"><i class="bi bi-star" :class="{'bi-star' : nimportant.isImportant}"></i></button>
          </span>
        </div> -->
        <!-- <TodayTodoPage/> -->
    </div>
</template>
  
<script>
import ImportantTodoPage from '@/views/ImportantTodoPage'
// import TodayTodoPage from '@/views/AllTodoPage'

export default {
    name: 'AllTodoPage',
    components: {
        ImportantTodoPage,
        // TodayTodoPage,
    },
    data() {
        return {
            adddata:null,
        }
    },
    computed: {
        // importanttodoList() {
        //     const importanttodolist = []
        //     this.$store.state.todo.list.forEach((todolist) => {
        //         if (todolist.isImportant === true) {
        //             importanttodolist.push(todolist)
        //         }
        //     })
        //     return importanttodolist
        // },
        // nimportanttodoList() {
        //     const nimportanttodolist = []
        //     this.$store.state.todo.list.forEach((todolist) => {
        //         if (todolist.isImportant === false) {
        //             nimportanttodolist.push(todolist)
        //         }
        //     })
        //     return nimportanttodolist
        // },
        todoList() {
            const todolist = []
            this.$store.state.todo.list.forEach((todo) => {
                todolist.push(todo)
            })
            return todolist
        }
    },
    methods: {
        addplan() {
            if (this.adddata != null) {
                this.$store.dispatch('addplan', this.adddata)
                this.adddata = null
            }
        },
        important(nimportant) {
            this.$store.dispatch('important',nimportant)
        }
    }
    }
</script>


<style>

  .bi-star-fill {
    color: black;
  }

</style>