'use strict'

/** @type {import('@adonisjs/lucid/src/Schema')} */
const Schema = use('Schema')

class StudentsSchema extends Schema {
  up () {
    this.create('students', (table) => {
      table.increments()
      table.string('username', 80)
      table.string('email', 80).unique()
      table.integer('age')
    })
  }

  down () {
    this.drop('students')
  }
}

module.exports = StudentsSchema
