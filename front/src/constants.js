const ALL_TALKS = `
{
  allTalks {
    id
    name
    speaker {
      name
    }
    timeSlot {
      id
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
