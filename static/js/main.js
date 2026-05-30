document.addEventListener("DOMContentLoaded", () => {

    const trainBtn = document.getElementById("trainBtn");

    if (trainBtn) {

        trainBtn.addEventListener("click", async () => {

            const loader =
                document.getElementById("loader");

            const result =
                document.getElementById("result");

            trainBtn.disabled = true;

            loader.classList.remove("hidden");

            result.innerHTML = "";

            try {

                const response =
                    await fetch("/train", {
                        method: "POST"
                    });

                const data =
                    await response.json();

                loader.classList.add("hidden");

                if (data.status === "success") {

                    result.innerHTML = `
                    <div class="success-card">

                    <h3>
                    Training Successful
                    </h3>

                    <p>
                    Status:
                    ${data.status}
                    </p>

                    <p>
                    Accuracy:
                    ${data.accuracy}%
                    </p>

                    </div>
                    `;
                }
                else {

                    result.innerHTML =
                    `<p class="error">
                    Training Failed
                    </p>`;
                }

            }

            catch(error){

                loader.classList.add("hidden");

                result.innerHTML =
                `<p class="error">
                ${error.message}
                </p>`;
            }

            finally{

                trainBtn.disabled = false;
            }

        });
    }


    const predictForm =
        document.getElementById("predictForm");

    if (predictForm) {

        predictForm.addEventListener(
        "submit",
        async(e)=>{

            e.preventDefault();

            const loader =
            document.getElementById(
            "predictLoader"
            );

            const result =
            document.getElementById(
            "predictionResult"
            );

            loader.classList.remove(
            "hidden"
            );

            const formData =
            new FormData(predictForm);

            try{

                const response =
                await fetch("/predict",{
                    method:"POST",
                    body:formData
                });

                const data =
                await response.json();

                loader.classList.add(
                "hidden"
                );

                const cls =
                data.prediction === "Phishing"
                ? "phishing"
                : "legitimate";

                result.innerHTML = `
                <div class="result-card ${cls}">
                ${data.prediction}
                </div>
                `;

            }

            catch(error){

                loader.classList.add(
                "hidden"
                );

                result.innerHTML =
                `<p class="error">
                Prediction Error
                </p>`;
            }

        });

    }

});