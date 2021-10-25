import { mapActions, mapState } from 'vuex'
import Chart from 'chart.js/auto'

export default {
  data () {
    return {
      data: [],
      states: [],
      myChart: null
    }
  },
  computed: {
    ...mapState('Airports', ['airports'])
  },
  methods: {
    ...mapActions('Airports', [
      'airportsDemography'
    ]),
    async setData (dados) {
      for (const airport of Object.entries(dados)) {
        this.data.push(airport)
      }
    },
    createLinePlot () {
      const ctx = document.getElementById('myChart').getContext('2d')
      this.myChart = new Chart(ctx, {
        type: 'line',
        data: {
          labels: this.states,
          datasets: [
            {
              label: 'Quantidade Aeroportos',
              backgroundColor: '#005EB8',
              borderColor: '#005EB8',
              pointStyle: 'circle',
              fill: true,
              data: this.data
            }
          ]
        },
        options: {
          responsive: true,
          stacked: true,
          tooltips: {
            enabled: false
          },
          plugins: {
            legend: {
              display: false,
              labels: {
                usePointStyle: true
              },
              position: 'top'
            }
          },
          elements: {
            line: {
              tension: 0.5
            }
          },
          scales: {
            y: {
              grid: {
                display: false
              }
            },
            x: {
              grid: {
                display: false
              }
            }
          }
        }
      })
      this.myChart.update()
    },
    async getAirports () {
      await this.airportsDemography()
      this.states = Object.keys(this.airports)
      await this.setData(this.airports)
      this.createLinePlot()
    }
  },
  created () {
    this.getAirports()
  }
}
