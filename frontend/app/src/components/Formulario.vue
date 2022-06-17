<template>
    <div>
        <v-card elevation="0">
            <v-card-title>Cadastro de Veículos</v-card-title>
            <v-divider class="ma-2"></v-divider>
            <v-form v-model="validacaoFormulario">
                <v-text-field
                    v-model="veiculo.veiculo"
                    :rules="regras.campo"
                    prepend-inner-icon="mdi-car-estate"
                    label="Veículo"
                    outlined
                    placeholder="Versa"
                ></v-text-field>
                <v-select
                    :items="listaMarcas"
                    :rules="regras.campo"
                    prepend-inner-icon="mdi-watermark"
                    item-text="texto"
                    item-value="valor"
                    v-model="veiculo.marca"
                    label="Selecione uma Marca"
                    outlined
                >
                </v-select>
                <v-text-field
                    v-model="veiculo.ano"
                    :rules="regras.campo"
                    type="number"
                    prepend-inner-icon="mdi-calendar"
                    label="Ano"
                    outlined
                    placeholder="2010"
                ></v-text-field>
                <v-textarea
                    v-model="veiculo.descricao"
                    :rules="regras.campo"
                    prepend-inner-icon="mdi-sticker-text-outline"
                    label="Descrição"
                    outlined
                    placeholder="Este é o carro do ano ..."
                ></v-textarea>
                <v-select
                    :items="valoresRadio"
                    item-text="texto"
                    item-value="valor"
                    v-model="veiculo.vendido"
                    label="Carro Vendido?" outlined>
                </v-select>
                <v-divider></v-divider>
                <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn text @click="cadastrar" :disabled="validacaoFormulario === false">
                        Cadastrar
                    </v-btn>
                </v-card-actions>
            </v-form>
        </v-card>
    </div>
</template>

<script>
import Veiculo from "@/domain/veiculo"
import {mapActions} from "vuex";
export default {
    name: "Formulario",
    data:() => ({
        veiculo: new Veiculo(),
        valoresRadio: [{"texto": "Sim", "valor": true}, {"texto": "Não", "valor": false}],
        listaMarcas: [
            {"texto": "Chevrolet", "valor": "Chevrolet"},
            {"texto": "Nissan", "valor": "Nissan"},
            {"texto": "Fiat", "valor": "Fiat"}
        ],
        validacaoFormulario: false,
        regras: {
            campo: [v => !!v || "Preencha o campo"]
        }
    }),
    methods: {
        ...mapActions(["cadastrarVeiculo", "retornarTodosVeiculos"]),

        cadastrar() {
            this.cadastrarVeiculo(this.veiculo).then(() => {
                this.veiculo = new Veiculo()
                this.retornarTodosVeiculos();
            })
        }
    }

}
</script>

<style scoped>

</style>