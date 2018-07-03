class Graph {
    constructor(nodes, connections, colors, colorsobject) {
        this.nodes = nodes;
        this.connections = connections;
        this.colors = colors;
		this.colorsobject = colorsobject
        this.coloredGraph = [];
    }

    colorable() {
        let colorCount = this.colors.length;
        let coloredGraph = [];
        // erstellt einen "Farblosen Graph"
        for (let i = 0; i < this.colors.length; i++) {
            coloredGraph.push([this.nodes[i], 'colorless'])
        }
        for (let node in coloredGraph) {
            // check neighbours
            for (let c = 0; c < this.connections.length; c++) {
                if (this.connections[c].includes(node)) {
                    //connection gefunden
                    let node2 = this.connections[c].remove(node)[0];
                }
            }
        }
        // Erzeugen eines Belegungsplans
        // Wähle Farbe: r
        for (let c; c < this.colors.length; c++) {
            let workingColor = this.color[c];
            // Belege ersten Farblosen Knoten: a
            for (let node = 0; nodeCount < coloredGraph.length; node) {
                if (coloredGraph[node].includes('colorless')) {
                    // bugged
                    coloredGraph[node] = coloredGraph[node].pop().push(workingColor);
                    console.log(coloredGraph);
                    break;
                }
                console.log()
            }
        }
		    // suche nächsten Farblosen Punkt => Wiederhole für Farbe: r, bis alle Knoten durchlaufen wurden
            // Prüfe ob alle Knoten gefärbt sind
			//-for each Color
			for (let color = 0; color < this.colors.length; color++) {
				const cyclecolor = this.colors[color];
				//--of each node
				for (let node = 0; node < coloredGraph.length; node++) {
					const workingnode = coloredGraph[node][0];
					if(coloredGraph[node].indexOf('colorless') > -1) {
						// fablosen Knoten gefunden
						// Prüfe alle Verbindungen (a,X), sodass Farbe a =/ Farbe X ; Abbruch bei gleicher Farbe und entfernen der Farbe
						//---of every connection
						for (let corners = 0; corners < this.connections.length; corners++) {
							// console.log('cycle Color: '+ cyclecolor);
							// console.log('for working node: ' + workingnode);
							// console.log('of connection: ' + this.connections[corners]);
							if(this.connections.indexOf(workingnode) > -1) {
								//connection found
								// copy connection
								const copyconnection = this.connections[corners].splice(0);
								if ( copyconnection.includes(workingnode)) {
								    // get the other node
									const othernode = copyconnection.toString.replace(workingnode, '').replace(',','');
									// check the color; if something is not colorless or different color than workingcolor resume
									if(this.colorsobject[othernode] == colorless && this.colorsobject != cyclecolor) {
										// everything is alright
										if()
									} else {
										// failed test
										break;
									}
								}
							}
						}
					}
				}
			}
        this.coloredGraph = coloredGraph;
        console.log(this.coloredGraph);
    }
}

// Knoten; Kanten; Farben
const testGraph = new Graph(
    ['a', 'b', 'c'],
    [['a', 'b'], ['b', 'c'], ['c', 'a']],
    ['r', 'g', 'b'],
	{ a: 'colorless', b: 'colorless', c: 'colorless'});
testGraph.colorable();