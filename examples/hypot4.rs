// stone:job stone:math.hypot4
// stone:function hypot4_rs

#[no_mangle]
pub extern "C" fn hypot4_rs(a: i32, b: i32, c: i32, d: i32) -> i32 {
    ((a * a + b * b + c * c + d * d) as f64).sqrt() as i32
}
