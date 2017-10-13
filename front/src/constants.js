const ALL_TALKS = `
{
  allTalks {
    id
    name
    speaker {
      name
    }
    timeSlot {
      date
      start
      end
    }
    room
    category
    isPlaceholder
  }
}`;

export default ALL_TALKS;
