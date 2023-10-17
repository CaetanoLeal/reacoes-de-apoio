def calcular_reacoes_apoio():
    tipo_distribuicao = input("Qual o tipo de distribuição da carga? (Simples / Distribuída): ")

    if tipo_distribuicao.lower() == "simples":
        num_vigas = int(input("Qual o número de vigas? "))
        comprimentos = []
        for _ in range(num_vigas):
            comprimento = float(input("Digite o comprimento da viga (em metros): "))
            comprimentos.append(comprimento)

        genero_apoio_1 = int(input("Qual o gênero do primeiro apoio? (1 para Gênero 1 / 2 para Gênero 2): "))
        genero_apoio_2 = int(input("Qual o gênero do segundo apoio? (1 para Gênero 1 / 2 para Gênero 2): "))

        if genero_apoio_1 == 1 and genero_apoio_2 == 1:
            carga_total = float(input("Digite o valor da carga total (em kN): "))
            reacao_apoio_1 = carga_total / 2
            reacao_apoio_2 = carga_total / 2
            reacao_centro = carga_total

            print("As reações de apoio são:")
            print("Reação do Apoio 1: ", reacao_apoio_1, "kN")
            print("Reação do Apoio 2: ", reacao_apoio_2, "kN")
            print("Reação no Centro: ", reacao_centro, "kN")

        elif genero_apoio_1 == 1 and genero_apoio_2 == 2:
            carga_total = float(input("Digite o valor da carga total (em kN): "))
            reacao_apoio_1 = carga_total / 3
            reacao_apoio_2 = (2 * carga_total) / 3
            reacao_centro = carga_total

            print("As reações de apoio são:")
            print("Reação do Apoio 1: ", reacao_apoio_1, "kN")
            print("Reação do Apoio 2: ", reacao_apoio_2, "kN")
            print("Reação no Centro: ", reacao_centro, "kN")

        elif genero_apoio_1 == 2 and genero_apoio_2 == 1:
            carga_total = float(input("Digite o valor da carga total (em kN): "))
            reacao_apoio_1 = (2 * carga_total) / 3
            reacao_apoio_2 = carga_total / 3
            reacao_centro = carga_total

            print("As reações de apoio são:")
            print("Reação do Apoio 1: ", reacao_apoio_1, "kN")
            print("Reação do Apoio 2: ", reacao_apoio_2, "kN")
            print("Reação no Centro: ", reacao_centro, "kN")

        else:
            print("Gênero de apoio inválido!")

    elif tipo_distribuicao.lower() == "distribuída":
        tipo_distribuicao_carga = input("Qual o tipo de distribuição da carga? (Perfeitamente / Geométrica): ")

        if tipo_distribuicao_carga.lower() == "perfeitamente":
            num_vigas = int(input("Qual o número de vigas? "))
            comprimentos = []
            for _ in range(num_vigas):
                comprimento = float(input("Digite o comprimento da viga (em metros): "))
                comprimentos.append(comprimento)

            genero_apoio_1 = int(input("Qual o gênero do primeiro apoio? (1 para Gênero 1 / 2 para Gênero 2): "))
            genero_apoio_2 = int(input("Qual o gênero do segundo apoio? (1 para Gênero 1 / 2 para Gênero 2): "))

            if genero_apoio_1 == 1 and genero_apoio_2 == 1:
                num_cargas = num_vigas + 1
                cargas = []
                for i in range(num_cargas):
                    carga = float(input(f"Digite o valor da carga {i+1} (em kN): "))
                    cargas.append(carga)

                reacao_apoio_1 = sum(cargas) / 2
                reacao_apoio_2 = sum(cargas) / 2
                reacao_centro = sum(cargas)

                print("As reações de apoio são:")
                print("Reação do Apoio 1: ", reacao_apoio_1, "kN")
                print("Reação do Apoio 2: ", reacao_apoio_2, "kN")
                print("Reação no Centro: ", reacao_centro, "kN")

            elif genero_apoio_1 == 1 and genero_apoio_2 == 2:
                num_cargas = num_vigas + 1
                cargas = []
                for i in range(num_cargas):
                    carga = float(input(f"Digite o valor da carga {i+1} (em kN): "))
                    cargas.append(carga)

                reacao_apoio_1 = sum(cargas) / 3
                reacao_apoio_2 = (2 * sum(cargas)) / 3
                reacao_centro = sum(cargas)

                print("As reações de apoio são:")
                print("Reação do Apoio 1: ", reacao_apoio_1, "kN")
                print("Reação do Apoio 2: ", reacao_apoio_2, "kN")
                print("Reação no Centro: ", reacao_centro, "kN")

            elif genero_apoio_1 == 2 and genero_apoio_2 == 1:
                num_cargas = num_vigas + 1
                cargas = []
                for i in range(num_cargas):
                    carga = float(input(f"Digite o valor da carga {i+1} (em kN): "))
                    cargas.append(carga)

                reacao_apoio_1 = (2 * sum(cargas)) / 3
                reacao_apoio_2 = sum(cargas) / 3
                reacao_centro = sum(cargas)

                print("As reações de apoio são:")
                print("Reação do Apoio 1: ", reacao_apoio_1, "kN")
                print("Reação do Apoio 2: ", reacao_apoio_2, "kN")
                print("Reação no Centro: ", reacao_centro, "kN")

            else:
                print("Gênero de apoio inválido!")

        elif tipo_distribuicao_carga.lower() == "geométrica":
            num_vigas = int(input("Qual o número de vigas? "))
            comprimentos = []
            for _ in range(num_vigas):
                comprimento = float(input("Digite o comprimento da viga (em metros): "))
                comprimentos.append(comprimento)

            genero_apoio_1 = int(input("Qual o gênero do primeiro apoio? (1 para Gênero 1 / 2 para Gênero 2): "))
            genero_apoio_2 = int(input("Qual o gênero do segundo apoio? (1 para Gênero 1 / 2 para Gênero 2): "))

            if genero_apoio_1 == 1 and genero_apoio_2 == 1:
                carga_total = float(input("Digite o valor da carga total (em kN): "))
                carga_inicial = float(input("Digite o valor da carga inicial (em kN): "))
                carga_final = float(input("Digite o valor da carga final (em kN): "))

                cargas = [carga_inicial]
                carga_atual = carga_inicial
                razao = carga_final / carga_inicial

                for _ in range(1, num_vigas):
                    carga_atual *= razao
                    cargas.append(carga_atual)

                cargas.append(carga_final)

                reacao_apoio_1 = sum(cargas) / 2
                reacao_apoio_2 = sum(cargas) / 2
                reacao_centro = sum(cargas)

                print("As reações de apoio são:")
                print("Reação do Apoio 1: ", reacao_apoio_1, "kN")
                print("Reação do Apoio 2: ", reacao_apoio_2, "kN")
                print("Reação no Centro: ", reacao_centro, "kN")

            elif genero_apoio_1 == 1 and genero_apoio_2 == 2:
                carga_total = float(input("Digite o valor da carga total (em kN): "))
                carga_inicial = float(input("Digite o valor da carga inicial (em kN): "))
                carga_final = float(input("Digite o valor da carga final (em kN): "))

                cargas = [carga_inicial]
                carga_atual = carga_inicial
                razao = carga_final / carga_inicial

                for _ in range(1, num_vigas):
                    carga_atual *= razao
                    cargas.append(carga_atual)

                cargas.append(carga_final)

                reacao_apoio_1 = sum(cargas) / 3
                reacao_apoio_2 = (2 * sum(cargas)) / 3
                reacao_centro = sum(cargas)

                print("As reações de apoio são:")
                print("Reação do Apoio 1: ", reacao_apoio_1, "kN")
                print("Reação do Apoio 2: ", reacao_apoio_2, "kN")
                print("Reação no Centro: ", reacao_centro, "kN")

            elif genero_apoio_1 == 2 and genero_apoio_2 == 1:
                carga_total = float(input("Digite o valor da carga total (em kN): "))
                carga_inicial = float(input("Digite o valor da carga inicial (em kN): "))
                carga_final = float(input("Digite o valor da carga final (em kN): "))

                cargas = [carga_inicial]
                carga_atual = carga_inicial
                razao = carga_final / carga_inicial

                for _ in range(1, num_vigas):
                    carga_atual *= razao
                    cargas.append(carga_atual)

                cargas.append(carga_final)

                reacao_apoio_1 = (2 * sum(cargas)) / 3
                reacao_apoio_2 = sum(cargas) / 3
                reacao_centro = sum(cargas)

                print("As reações de apoio são:")
                print("Reação do Apoio 1: ", reacao_apoio_1, "kN")
                print("Reação do Apoio 2: ", reacao_apoio_2, "kN")
                print("Reação no Centro: ", reacao_centro, "kN")

            else:
                print("Gênero de apoio inválido!")

        else:
            print("Tipo de distribuição de carga inválido!")

    else:
        print("Tipo de distribuição inválido!")


calcular_reacoes_apoio()