// stone:job stone:math.wrap_pi
// stone:function wrap_pi_rs

#[no_mangle]
pub extern "C" fn wrap_pi_rs(a: f64) -> f64 {
    const PI: f64 = std::f64::consts::PI;
    let mut r = a.rem_euclid(2.0 * PI);
    if r > PI { r -= 2.0 * PI; }
    r
}
