export default function createReportObject(employeesList) {
  return ({
    allEmployees: employeesList,
    getNumberOfDepartment: (all) => Object.keys(all).length,
  });
}
