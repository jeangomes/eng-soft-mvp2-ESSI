const myRequest = (codeFilter) => {
    let url = 'http://localhost:5000/operations'
    if (codeFilter !== '') {
        url = 'http://localhost:5000/operations?code=' + codeFilter
    }
    return fetch(url)
        .then(data => {
            return data.json();
        })
        .then(myData => {
            return  myData.operations;
        })
        .catch(function (error) {
            console.log(error.message)
        });
}

const postMyData = (myState) => {
    const form_data = new FormData();
    for ( let key in myState ) {
        form_data.append(key, myState[key]);
    }
    const options = {
        method: 'POST',
        body: form_data
    };
    return fetch('http://localhost:5000/crianca', options)
        .then(data => {
            return data.json();
        })
        .then(myData => {
            return  myData;
        })
        .catch(e => {
            console.log(e);
        });
}
