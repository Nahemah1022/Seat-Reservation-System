import request from "@/api/request";

export function getAllStudent() {
  return request({
    url: "/users",
    method: "GET",
  });
}

export function createStudent(id, name, password) {
  return request({
    url: "/users/register",
    method: "POST",
    data: {
      id: id,
      name: name,
      password: password,
    },
  });
}

export function loginStudent(id, password) {
  return request({
    url: "/users/login",
    method: "POST",
    data: {
      id: id,
      password: password,
    },
  });
}

export function getAllCourse() {
  return request({
    url: "/course/getAllCourse",
    method: "GET",
  });
}

export function getCourse(course_id, date) {
  return request({
    url: "/course/getCourse",
    method: "GET",
    params: { course_id: course_id, date: date },
  });
}

export function addCourse(id, date, name, classroom, seats, cols) {
  return request({
    url: "/addCourse",
    method: "POST",
    id: id,
    data: {
      date: date,
      name: name,
      classroom: classroom,
      seats: seats,
      cols: cols,
    },
  });
}

export function bookSeat(course_id, course_date, seat_id, reserved_by) {
  return request({
    url: "/seat/book",
    method: "POST",
    data: {
      course_id: course_id,
      course_date: course_date,
      seat_id: seat_id,
      reserved_by: reserved_by,
    },
  });
}

export function cancelBookedSeat(course_id, course_date, seat_id, reserved_by) {
  return request({
    url: "/seat/cancel",
    method: "POST",
    data: {
      course_id: course_id,
      course_date: course_date,
      seat_id: seat_id,
      reserved_by: reserved_by,
    },
  });
}
