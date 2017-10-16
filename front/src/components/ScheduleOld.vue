<template>
  <div class="schedule">
    <div class="row">
      <h2>{{title}}</h2>
      <div class="cell">Hora</div>
      <div class="cell" v-for="(room, index) in roomIds">
        {{roomNames[index]}}
      </div>
    </div>
    <div class="row" v-for="slot in orderedTimeSlots()">
      <div class="cell">{{slot.start.substring(0, 5)}}-{{slot.end.substring(0, 5)}}</div>
      <div v-show="grid[slot.id]['A_']" class="cell full">
        <p>{{grid[slot.id]['A_'] && grid[slot.id]['A_'].speaker}}</p>
        <p class="name">{{grid[slot.id]['A_'] && grid[slot.id]['A_'].name}}</p>
      </div>
      <div v-show="!grid[slot.id]['A_']">
        <div class="cell" v-for="room in roomIds">
          <p>{{grid[slot.id] && grid[slot.id][room] && grid[slot.id][room].speaker}}</p>
          <p class="name">{{grid[slot.id] && grid[slot.id][room] && grid[slot.id][room].name}}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

export default {
  name: 'schedule',
  props: ['title', 'roomNames', 'roomIds', 'timeSlots', 'grid'],
  data() {
    return {
    }
  },
  methods: {
    orderedTimeSlots() {
      var orderedTimeSlots = Object.values(this.timeSlots);
      //order by time
      orderedTimeSlots.sort((a, b) => {
        let nameA = `${a.date} ${a.start} ${a.end}`;
        let nameB = `${b.date} ${b.start} ${b.end}`;
        if (nameA < nameB) {
          return -1;
        }
        if (nameA > nameB) {
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
.schedule {
  clear: both;
}

.row .cell {
  border: 1px solid black;
  padding: 5px;
  float: left;
  box-sizing: border-box;
  width: 17%;
  height: 130px;
}

.row .cell.full {
  width: 68%;
}

.row {
  clear: both;
}

.cell .name {
  font-weight: bold;
}
</style>