<template>
  <div class="hello">
		<div class="notification is-success" style="z-index:100; position: fixed; left: 0; right: 0; margin: auto" v-if="show">
			<button class="delete"></button>
			Your Predicted Salary is: ${{pred}} USD / SoCal Adjusted ${{ pred * 1.15 }}
		</div>
		<div class="columns">
			<div class="column"></div>
			<div class="column is-half">
				<div class="card">
					<header class="card-header">
						<p class="card-header-title">
							Find Out Salary!
						</p>
					</header>
					<div class="card-content">
						<div class="content">
							<!-- Program Hobby-->
							<div class="field is-horizontal">
								<label class="field-label">Do you Program as a hobby?</label>
								<div class="control">
									<div class="select field-body">
										<select v-model="vars[0]">
											<option>Select One</option>
											<option value="1">Yes!</option>
											<option value="2">Nope</option>
										</select>
									</div>
								</div>
							</div>


							<div class="field is-horizontal">
								<label class="field-label">How many Years have you been programming</label>
								<div class="control">
									<div class="select field-body">
										<select v-model="vars[1]">
											<option v-for="x in 22">{{x}}</option>
										</select>
									</div>
								</div>
							</div>


							<div class="field is-horizontal">
								<label class="field-label">How many years have you been a professional developer</label>
								<div class="control">
									<div class="select field-body">
										<select v-model="vars[2]">
											<option v-for="x in 22">{{x}}</option>
										</select>
									</div>
								</div>
							</div>

							<h1 class="title is-4">
								What kind of developer do you identify as?
							</h1>

							<div class="field is-horizontal">
								<label class="field-label">Web Developer</label>
								<div class="control">
									<div class="select field-body">
										<select v-model="vars[3]">
										<option>Select One</option>
										<option value="1">Yes</option>
										<option value="0">Nope</option>
										</select>
									</div>
								</div>
							</div>

							<div class="field is-horizontal">
								<label class="field-label">Mobile Dev</label>
								<div class="control">
									<div class="select field-body">
										<select v-model="vars[4]">
										<option>Select One</option>
										<option value="1">Yes</option>
										<option value="0">Nope</option>
										</select>
									</div>
								</div>
							</div>

							<div class="field is-horizontal">
								<label class="field-label">Machine Learning Specialist</label>
								<div class="control">
									<div class="select field-body">
										<select v-model="vars[5]">
										<option>Select One</option>
										<option value="1">Yes</option>
										<option value="0">Nope</option>
										</select>
									</div>
								</div>
							</div>

							<div class="field is-horizontal">
								<label class="field-label">DevOps</label>
								<div class="control">
									<div class="select field-body">
										<select v-model="vars[6]">
										<option>Select One</option>
										<option value="1">Yes</option>
										<option value="0">Nope</option>
										</select>
									</div>
								</div>
							</div>

							<div class="field is-horizontal">
								<label class="field-label">Desktop Developer</label>
								<div class="control">
									<div class="select field-body">
										<select v-model="vars[7]">
										<option>Select One</option>
										<option value="1">Yes</option>
										<option value="0">Nope</option>
										</select>
									</div>
								</div>
							</div>

							<div class="field is-horizontal">
								<label class="field-label">Database Base Administrator</label>
								<div class="control">
									<div class="select field-body">
										<select v-model="vars[8]">
										<option>Select One</option>
										<option value="1">Yes</option>
										<option value="0">Nope</option>
										</select>
									</div>
								</div>
							</div>

							<div class="field is-horizontal">
								<label class="field-label">Some Other Kind?</label>
								<div class="control">
									<div class="select field-body">
										<select v-model="vars[9]">
										<option>Select One</option>
										<option value="1">Yes</option>
										<option value="0">Nope</option>
										</select>
									</div>
								</div>
							</div>

						<h1 class="title is-4">Education</h1>

							<div class="field is-horizontal">
								<label class="field-label">Do you have a Bachelors?</label>
								<div class="control">
									<div class="select field-body">
										<select v-model="vars[10]">
										<option>Select One</option>
										<option value="1">Yes</option>
										<option value="0">Nope</option>
										</select>
									</div>
								</div>
							</div>

							 <div class="field is-horizontal">
								<label class="field-label">Masters Degree</label>
								<div class="control">
									<div class="select field-body">
										<select v-model="vars[11]">
										<option>Select One</option>
											<option value="1">Yes</option>
											<option value="0">Nope</option>
										</select>
									</div>
								</div>
							</div>

						<div class="field is-horizontal">
							<label class="field-label">Doctorate / Professional Degree</label>
							<div class="control">
								<div class="select field-body">
									<select v-model="vars[12]">
										<option>Select One</option>
										<option value="1">Yes</option>
										<option value="0">Nope</option>
									</select>
								</div>
							</div>
						</div>

						<h1 class="title is-4">Wait... but why?</h1>

						<div class="field is-horizontal">
							<label class="field-label">Do you use Tabs primarily?</label>
							<div class="control">
								<div class="select field-body">
									<select v-model="vars[13]">
									<option>Select One</option>
										<option value="1">Yes</option>
										<option value="0">Nope</option>
									</select>
								</div>
							</div>
						</div>
							<h1 class="title is-4">Do you currently work for a...</h1>
							<div class="field is-horizontal">
								<label class="field-label">Small Company ()</label>
								<div class="control">
									<div class="select field-body">
										<select v-model="vars[14]">
										<option>Select One</option>
										<option value="1">Yes</option>
										<option value="0">Nope</option>
										</select>
									</div>
								</div>
							</div>

							<div class="field is-horizontal">
								<label class="field-label">Medium Sized Company</label>
								<div class="control">
									<div class="select field-body">
										<select v-model="vars[15]">
										<option>Select One</option>
										<option value="1">Yes</option>
										<option value="0">Nope</option>
										</select>
									</div>
								</div>
							</div>

							<div class="field is-horizontal">
								<label class="field-label">Large Company</label>
								<div class="control">
									<div class="select field-body">
										<select v-model="vars[16]">
										<option>Select One</option>
										<option value="1">Yes</option>
										<option value="0">Nope</option>
										</select>
									</div>
								</div>
							</div>

						<blockquote>
							In a complete twist of irony...
							Stack overflow built the same calculator and sent us an email yesterday,
							knowing that the speech was going to happen
						</blockquote>
						</div>
					</div>
					<footer class="card-footer">
						<a href="#" class="card-footer-item" @click="predict">Predict</a>
						<a href="#" class="card-footer-item" @click="retrain">Retrain &amp; Predict</a>
					</footer>
				</div>
			</div>
			<div class="column"></div>
		</div>
		<br>
		<br>
		<br>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: 'HelloWorld',
	data(){
		return {
			url: 'http://127.0.0.1:8000',
			vars: [],
			pred: 0,
			show: false,
		}
	},
	methods: {
		predict() {
			let arr = this.vars.map(item => Math.ceil(item))
			axios.post(`${this.url}/predict`, { vars: arr })
				.then((response) => {
					this.pred = Math.ceil(response.data[0][0]);

					this.toggle();

					setTimeout(() => {
						this.toggle()
					}, 5000);
				})
				.catch(error => console.log(error))
		},
		retrain(){
			let arr = this.vars.map(item => Math.ceil(item))
			var Salary = prompt("What is your salary?");
			axios.post(`${this.url}/retrain`, {
					vars: arr,
					Salary: Salary
				})
				.then((response) => {
					this.pred = Math.ceil(response.data[0][0]);

					this.toggle();

					setTimeout(() => {
						this.toggle()
					}, 5000);
				})
			.catch(error => console.log(error))
		},
		toggle(){
			this.show = !this.show
		}
	}
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
