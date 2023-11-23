const contextoPie1 = document.getElementById('pieChartOne')
const archs = guestData.map( (e) => { return e.arch } )
const arch = [...new Set(archs)]
const quantperArch = []

arch.forEach((e) => {
    quantperArch.push(countOccurrences(archs, e))
})

const dataPie1 = {
    labels: arch,
    datasets:[{
        label: "Arch",
        data: quantperArch,
        backgroundColor: [
        'rgb(255, 99, 132)',
        'rgb(54, 162, 235)',
        'rgb(255, 205, 86)'
      ],
        hoverOffset: 4
    }]
}

const configPie1 = {
    type: 'doughnut',
    data: dataPie1
}

new Chart(contextoPie1, configPie1)