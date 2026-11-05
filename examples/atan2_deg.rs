// stone:job stone:math.atan2_deg
// stone:function atan2_deg_rs

#[no_mangle]
pub extern "C" fn atan2_deg_rs(y: i32, x: i32) -> i32 {
    let mut r = (y as f64).atan2(x as f64).to_degrees();
    if r <= -180.0 {
        r += 360.0;
    }
    r as i32
}
