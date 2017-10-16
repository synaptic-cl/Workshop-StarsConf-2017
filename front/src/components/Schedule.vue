<template>
  <div class="schedule">
    <div class="row">
      <div></div>
      <div v-for="room in roomIds">
        {{room}}
      </div>
    </div>
    <div class="row" v-for="slot in orderedTimeSlots()">
        <div>{{slot.date}} {{slot.start}}-{{slot.end}}</div>
        <div class="talk" v-for="room in roomIds">
          <p>{{grid[slot.id] && grid[slot.id][room] && grid[slot.id][room].speaker && grid[slot.id][room].speaker.name}}</p>
          <p class="name">{{grid[slot.id] && grid[slot.id][room] && grid[slot.id][room].name}}</p>
        </div>
    </div>
  </div>
</template>

<script>

export default {
  name: 'schedule',
  props: ['roomNames', 'roomIds', 'timeSlots', 'grid'],
  data() {
    return {
    }
  },
  methods: {
    orderedTimeSlots() {
      var orderedTimeSlots = Object.values(this.timeSlots);
      //order by time
      orderedTimeSlots.sort((a,b) => {
        let nameA = `${a.date} ${a.start} ${a.end}`;
        let nameB = `${b.date} ${b.start} ${b.end}`;
        if(nameA < nameB){
          return -1;
        }
        if(nameA > nameB){
          return 1;
        }
        return 0;
      });
      return orderedTimeSlots;
    }
  }
}
</script>


<style>
.row div {
  border: 1px solid black;
  float: left;
  box-sizing: border-box;
  width: 17%;
  height: 120px;
}
.row {
  clear: both;
}

.talk .name {
 font-weight: bold;
}

</style>