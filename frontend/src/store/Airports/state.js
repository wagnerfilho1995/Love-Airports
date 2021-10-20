const airports = localStorage.getItem('airport') || '[]'

export default {
  airports: JSON.parse(airports)
}
