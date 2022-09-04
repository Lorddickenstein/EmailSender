function createEmail() {
	const sendForm = document.querySelector('.send-form')
	sendForm.style.display = 'flex'

	const btnCreateEmail = document.querySelector('.button-create')
	btnCreateEmail.style.display = 'none'
}

function uploadImage() {
	console.log('uploadImage')
}

function uploadAttachment() {
	console.log('uploadAttachment')
}

function countDown() {
	const circle = document.querySelector('.circle')
	timeLeft = circle.innerText

	const submitButton = document.querySelector('#button-submit')

	timerId = setInterval(() => {
		timeLeft--
		circle.innerText = timeLeft

		if (timeLeft == 0){
			clearInterval(timerId)
			submitButton.classList.add('status-submit-enabled')
			submitButton.disabled = false
		}
	}, 1000)
}
