const contextoPie2 = document.getElementById('pieChartTwo')
const repoGroups = guestData.map( (e) => { return e.groups } )
const quantperGroup = []
const repos = []

repoGroups.map((e) => {

    if (typeof(e) == "string"){
        repos.push(e.replace('@', ''))
    }else{
        if (e.length > 0){
            for(let i=0; i < e.length; i++){
                repos.push(e[i])
            }
        }    
    }
})

const repo = [...new Set(repos)]

repo.forEach((e) => {
    quantperGroup.push(countOccurrences(repos, e))
})


const dataPie2 = {
    labels: repo,
    datasets:[{
        label: "Quantity of packages",
        data: quantperGroup,
        backgroundColor:[],
        hoverOffset: 4
    }]
}

repo.forEach((e) => {
     dataPie2["datasets"][0].backgroundColor.push('rgb'+rcolors().split('\t')[3])       
})

const configPie2 = {
    type: 'doughnut',
    data: dataPie2
}

new Chart(contextoPie2, configPie2)
