'use strict'

const Student = use('App/Models/Student')

class StudentController {
  async index() {
    return await Student.all()
  }
}

module.exports = StudentController
