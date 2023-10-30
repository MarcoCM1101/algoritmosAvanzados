from typing import Optional
from graph import Graph
from generic_search import bfs, Node, node_to_path

if __name__ == "__main__":
    metrorrey: Graph[str] = Graph(["Talleres",
                                   "San Bernabé",
                                   "Unidad Modelo",
                                   "Aztlán",
                                   "Peniteniana",
                                   "Alfonso Reyes",
                                   "Mitras",
                                   "Simón Bolivar",
                                   "Hospital",
                                   "Edison",
                                   "Central",
                                   "Cuauhtémoc",
                                   "Del Golfo",
                                   "General Anaya",
                                   "Regina",
                                   "Niños Héroes",
                                   "Universidad",
                                   "Anáhuac",
                                   "San Nicolás",
                                   "Santiago Tapia",
                                   "Sendero",
                                   "Alameda",
                                   "Fundadores",
                                   "Padre Mier",
                                   "General I. Zaragoza",
                                   "Santa Lucía",
                                   "Colonia Obrera",
                                   "Félix U. Gómez",
                                   "Parque Fundidora",
                                   "Y Griega",
                                   "Eloy Cavazos",
                                   "Lerdo de Tejada",
                                   "Exposición",
                                   "Metalúrgicos",
                                   "Colonia Moderna",
                                   "Ruiz Cortines",
                                   "Los Ángeles",
                                   "Hospital Metropolitano"])

    metrorrey.add_edge_by_vertices("Talleres",
                                   "San Bernabé")
    metrorrey.add_edge_by_vertices("San Bernabé",
                                   "Unidad Modelo")
    metrorrey.add_edge_by_vertices("Talleres",
                                   "San Bernabé")
    metrorrey.add_edge_by_vertices("San Bernabé",
                                   "Unidad Modelo")
    metrorrey.add_edge_by_vertices("Unidad Modelo",
                                   "Aztlán")
    metrorrey.add_edge_by_vertices("Aztlán",
                                   "Peniteniana")
    metrorrey.add_edge_by_vertices("Peniteniana",
                                   "Alfonso Reyes")
    metrorrey.add_edge_by_vertices("Alfonso Reyes",
                                   "Mitras")
    metrorrey.add_edge_by_vertices("Mitras",
                                   "Simón Bolivar")
    metrorrey.add_edge_by_vertices("Simón Bolivar",
                                   "Hospital")
    metrorrey.add_edge_by_vertices("Hospital",
                                   "Edison")
    metrorrey.add_edge_by_vertices("Edison",
                                   "Central")
    metrorrey.add_edge_by_vertices("Central",
                                   "Cuauhtémoc")
    metrorrey.add_edge_by_vertices("Cuauhtémoc",
                                   "Del Golfo")
    metrorrey.add_edge_by_vertices("Cuauhtémoc",
                                   "General Anaya")
    metrorrey.add_edge_by_vertices("General Anaya",
                                   "Regina")
    metrorrey.add_edge_by_vertices("Regina",
                                   "Niños Héroes")
    metrorrey.add_edge_by_vertices("Niños Héroes",
                                   "Universidad")
    metrorrey.add_edge_by_vertices("Universidad",
                                   "Anáhuac")
    metrorrey.add_edge_by_vertices("Anáhuac",
                                   "San Nicolás")
    metrorrey.add_edge_by_vertices("San Nicolás",
                                   "Santiago Tapia")
    metrorrey.add_edge_by_vertices("Santiago Tapia",
                                   "Sendero")
    metrorrey.add_edge_by_vertices("Cuauhtémoc",
                                   "Alameda")
    metrorrey.add_edge_by_vertices("Alameda",
                                   "Fundadores")
    metrorrey.add_edge_by_vertices("Fundadores",
                                   "Padre Mier")
    metrorrey.add_edge_by_vertices("Padre Mier",
                                   "General I. Zaragoza")
    metrorrey.add_edge_by_vertices("General I. Zaragoza",
                                   "Santa Lucía")
    metrorrey.add_edge_by_vertices("Santa Lucía",
                                   "Colonia Obrera")
    metrorrey.add_edge_by_vertices("Colonia Obrera",
                                   "Félix U. Gómez")
    metrorrey.add_edge_by_vertices("Del Golfo",
                                   "Félix U. Gómez")
    metrorrey.add_edge_by_vertices("Félix U. Gómez",
                                   "Metalúrgicos")
    metrorrey.add_edge_by_vertices("Metalúrgicos",
                                   "Colonia Moderna")
    metrorrey.add_edge_by_vertices("Colonia Moderna",
                                   "Ruiz Cortines")
    metrorrey.add_edge_by_vertices("Ruiz Cortines",
                                   "Los Ángeles")
    metrorrey.add_edge_by_vertices("Los Ángeles",
                                   "Hospital Metropolitano")
    metrorrey.add_edge_by_vertices("Félix U. Gómez",
                                   "Parque Fundidora")
    metrorrey.add_edge_by_vertices("Parque Fundidora",
                                   "Y Griega")
    metrorrey.add_edge_by_vertices("Y Griega",
                                   "Eloy Cavazos")
    metrorrey.add_edge_by_vertices("Eloy Cavazos",
                                   "Lerdo de Tejada")
    metrorrey.add_edge_by_vertices("Lerdo de Tejada",
                                   "Exposición")

    result: Optional[Node[str]] = bfs(
        "Lerdo de Tejada",
        lambda x: x == "Padre Mier", metrorrey.neighbors_for_vertex
    )
    if result:
        path: list[str] = node_to_path(result)
        print(path)
    else:
        print("No solution found")
