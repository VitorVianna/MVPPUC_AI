let enderecoAPI = "http://192.168.1.6:5000/"
function Calcular(){
    var selectedCasa = $('input[name="rdbCasa"]:checked');
    var selectedRenda = $('input[name="rdbRenda"]:checked');
    var selectedTrabalho = $('input[name="rdbTrabalho"]:checked');

    let estado = $("#cmbEstado").val();
    let idade = $("#txtIdade").val();
    let faixaEtaria = $("#cmbFaixaEtaria").val();
    let escolaridade = $("#cmbEscolaridade").val();
    let estadoCivil = $("#cmbEstadoCivil").val();
    let qtdFilhos = $("#txtQtdFilhos").val();
    let possuiCasa = $('label[for="' + selectedCasa.attr('id') + '"]').text().trim() == "Sim" ? 1 : 0;
    let valImoveis = $("#txtValorTotalImoveis").val();
    let qtdImoveis = $("#txtQtdImoveis").val();
    let rendaExtra = $('label[for="' + selectedRenda.attr('id') + '"]').text().trim() == "Sim" ? 1 : 0;
    let valRendaExtra = $("#txtValorRendaExtra").val();
    let valMesesEmprego = $("#txtMesesEmprego").val();
    let trabalha = $('label[for="' + selectedTrabalho.attr('id') + '"]').text().trim() == "Sim" ? 1 : 0;
    let valSalario = $("#txtSalario").val();
    let qtdAutomoveis = $("#txtQtdAutomoveis").val();
    let valAutomoveis = $("#txtValorAutomoveis").val();

    let url = enderecoAPI + "get_credit?estado="+estado+"&idade="+idade+"&faixaEtaria="+faixaEtaria+"&escolaridade="+escolaridade+"&estadoCivil="+estadoCivil
                            +"&qtdFilhos="+qtdFilhos+"&possuiCasa="+possuiCasa+"&valImoveis="+valImoveis+"&qtdImoveis="+qtdImoveis+"&rendaExtra="+rendaExtra
                            +"&valRendaExtra="+valRendaExtra+"&valMesesEmprego="+valMesesEmprego+"&trabalha="+trabalha+"&valSalario="+valSalario+"&qtdAutomoveis="+qtdAutomoveis
                            +"&valAutomoveis="+valAutomoveis;
        fetch(url, {
            method: 'get'
        })
        .then((response) => response.json())
        .then((data) => {
            
            alert(data.Analise);
        })
        .catch((error) => {
        console.error('Error:', error);
        });
}