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
        label: "Quantity of packages",
        data: quantperArch,
        backgroundColor: [],
        hoverOffset: 4
    }]
}

arch.forEach((e) => {
    dataPie1["datasets"][0].backgroundColor.push('rgb'+rcolors().split('\t')[3])       
})

const configPie1 = {
    type: 'doughnut',
    data: dataPie1
}

new Chart(contextoPie1, configPie1)