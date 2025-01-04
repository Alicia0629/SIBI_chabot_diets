#!/bin/bash
set -e

while true; do
    echo "----------------------------"
    echo "   Menú de Opciones"
    echo "----------------------------"
    echo "1) Configurar el entorno inicial y crear el RAG"
    echo "2) Ejecutar la aplicación web"
    echo "3) Ejecutar tests sobre los distintos métodos"
    echo "4) Generar informe de cobertura de pruebas"
    echo "5) Abriendo informe de cobertura"
    echo "6) Salir"
    echo "----------------------------"
    read -p "Selecciona una opción: " opcion

    case $opcion in
        1) 
            echo "Ejecutando setup.sh..."
            ./setup.sh
            ;;
        2) 
            echo "Ejecutando runWeb.sh..."
            ./runWeb.sh
            ;;
        3) 
            echo "Ejecutando tests.sh..."
            ./tests.sh
            ;;
        4) 
            echo "Ejecutando coverage.sh..."
            ./coverage.sh
            ;;
        5) 
	    echo "Abriendo informe de cobertura..."
	    xdg-open htmlcov/index.html
	    ;;
	6)
            echo "Saliendo..."
            exit 0
            ;;
        *) 
            echo "Opción inválida. Por favor, intenta de nuevo."
            ;;
    esac
done

