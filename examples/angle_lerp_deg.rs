// stone:job stone:math.angle_lerp_deg
// stone:function angle_lerp_deg_rs

#[no_mangle]
pub extern "C" fn angle_lerp_deg_rs(a: f64, b: f64, t: f64) -> f64 {
    let diff = (b - a + 180.0).rem_euclid(360.0) - 180.0;
    (a + diff * t).rem_euclid(360.0)
}
