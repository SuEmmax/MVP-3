function forecast() {
    const form = document.getElementById("classification-form");
    const formData = new FormData(form);

    const data = {};
    formData.forEach((value, key) => {
      data[key] = parseFloat(value);
    });

    let url = "http://127.0.0.1:5000/classify";
    fetch(url, {
      headers: {
        "Content-Type": "application/json",
      },
      method: "post",
      body: JSON.stringify(data),
    })
      .then((response) => {
        if (!response.ok) {
          throw new Error("Response from backend was not ok");
        }
        return response.json();
      })
      .then((data) => {
        const classification = data.classification;

        let classificationResult;
        switch (Math.floor(classification)) {
          case 0:
            classificationResult = "Benign";
            document.getElementById("result").className = "result-healthy";
            break;
          case 1:
            classificationResult = "Malign";
            document.getElementById("result").className = "result-suspect";
            break;
          default:
            classificationResult = "Unknown";
            break;
        }
        document.getElementById(
          "result"
        ).innerText = `Classification: ${classificationResult}`;
      })
      .catch((error) => {
        document.getElementById("result").className = "error";
        document.getElementById("result").innerText = "An error occurred. Please check input data and try again.";
      });

  }