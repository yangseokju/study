<template>
  <div id="app">
    <h1>SSAFY 상담 예약 시스템</h1>
    <div style="width:auto; height:570px;">
      <div class="box divleft" style="height:inherit; padding:50px;">
        <h2>예약 페이지</h2>
        <h3>선생님 선택</h3>
        <div>
          <button v-for="(teacher, index) in teachers" :key="index"
          class="selected1"
          @click="btnclick2"
          :class="{'selected2':isSelected2(teacher)}">{{teacher}}</button>
        </div>
        <hr>
        <h3>시간 선택</h3>
        <div>
          <button v-for="(time, i) in times" :key="i"
          class="selected1" 
          @click="btnclick"
          :class="{'selected2':isSelected1(time)}">{{time}}</button>
        </div>
      </div>
      <div class="box divright" style="height:inherit; padding:50px;">
        <h2>상담 신청 현황</h2>
        <h3>상담 선생님</h3>
        <h4>성함 : 
          {{selected2[0]}}
        </h4>
        <hr>
        <h3>예약 현황</h3>
        <h4>시간들 : 
          <span v-for="(select, j) in selected" :key="j">
          {{select}}
          </span>
        </h4>
        <hr>
        <img alt="ssafy_logo" src="./assets/ssafy-logo.png">
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'App',
  data: function() {
      return {times: [
        "09:00","09:30","10:00","10:30","11:00","11:30","12:00","12:30","13:00","13:30",
        "14:00","14:30","15:00","15:30","16:00","16:30","17:00","17:30",
      ],
      selected : [],
      teachers : ["Eric", "Tony"],
      selected2 : [],
    }
  },
  methods: {
    btnclick: function(timedata) {
      const time = timedata.currentTarget.textContent
      if (this.selected.includes(time)) {
        this.selected.splice(this.selected.indexOf(time),1)
      } else {
          if (this.selected.length == 5) {
          alert('5타임까지만 신청할 수 있습니다.')
          } else{
            this.selected.push(time)
          }
      }
    },
    isSelected1: function(timedata) {
      if (this.selected.includes(timedata)) {
        return true
      } else {
        return false
      }
    },
    btnclick2: function(teacherdata) {
      const teacher = teacherdata.currentTarget.textContent
      if (this.selected2.includes(teacher)) {
        this.selected2.splice(this.selected2.indexOf(teacher),1)
      } else if (this.selected2.length == 1) {
        this.selected2.pop()
        this.selected2.push(teacher)
      } else {
        this.selected2.push(teacher)
      }
    },
    isSelected2: function(teacherdata) {
      if (this.selected2.includes(teacherdata)) {
        return true
      } else {
        return false
      }
    },
    }
  }

</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}


.divleft {
  width: 50%;
  float: left;
  box-sizing: border-box;
  box-shadow: 3px 3px 3px 3px #8e9092;
}

.divright {
  width: 50%;
  float: right;
  box-sizing: border-box;      
  background: rgb(205, 219, 230);
  box-shadow: 3px 3px 3px 3px #8e9092;
}

.selected1:hover{
  color : #0F4c81;
  background-color: #658dc63d;
}

.selected1 {
  color : #838383;
  background-color: rgba(0,0,0,0);
  border : 1px solid rgba(0,0,0,0);
  padding : 8px;
}

.selected2 {
  color : #838383;
  border: 1px solid rgb(58, 143, 182);
  background-color: rgb(185, 226, 245);
  padding : 8px;
}

hr {
  height: 1px;
  border: 0px;
  background:rgb(111, 111, 240);
}
</style>
