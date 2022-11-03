<template>
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
        <br>
        <button @click="fromParent">예약 확정</button>
      </div>
</template>

<script>

export default {
    name:'TimeTable',
    components: {
    },
    data: function () {
        return { times: [
                "09:00",
                "09:30",
                "10:00",
                "10:30",
                "11:00",
                "11:30",
                "12:00",
                "12:30",
                "13:00",
                "13:30",
                "14:00",
                "14:30",
                "15:00",
                "15:30",
                "16:00",
                "16:30",
                "17:00",
                "17:30",
            ], selected: [], teachers: ["Eric", "Tony"], selected2: [],
        }},
    methods: {
        btnclick: function (timedata) {
            const time = timedata.currentTarget.textContent;
            if (this.selected.includes(time)) {
                this.selected.splice(this.selected.indexOf(time), 1);
            }
            else {
                if (this.selected.length == 5) {
                    alert("5타임까지만 신청할 수 있습니다.");
                }
                else {
                    this.selected.push(time);
                }
            }
        },
        isSelected1: function (timedata) {
            if (this.selected.includes(timedata)) {
                return true;
            }
            else {
                return false;
            }
        },
        btnclick2: function (teacherdata) {
            const teacher = teacherdata.currentTarget.textContent;
            if (this.selected2.includes(teacher)) {
                this.selected2.splice(this.selected2.indexOf(teacher), 1);
            }
            else if (this.selected2.length == 1) {
                this.selected2.pop();
                this.selected2.push(teacher);
            }
            else {
                this.selected2.push(teacher);
            }
        },
        isSelected2: function (teacherdata) {
            if (this.selected2.includes(teacherdata)) {
                return true;
            }
            else {
                return false;
            }
        },
        fromParent() {
            this.$emit("from-parent1",this.selected)
            this.$emit("from-parent2",this.selected2)
            this.selected = []
            this.selected2 = []
        },
    }
}

</script>

<style>

</style>