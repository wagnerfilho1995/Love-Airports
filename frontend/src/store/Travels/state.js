const travels = localStorage.getItem('travel') || '[]'

export default {
  travels: JSON.parse(travels)
}
