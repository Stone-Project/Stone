// stone:job stone:math.clamp_angle
// stone:function clamp_angle_rs

#[no_mangle]
pub extern "C" fn clamp_angle_rs(a: i32, lo: i32, hi: i32) -> i32 {
    let span = (hi - lo).rem_euclid(360);
    let off = (a - lo).rem_euclid(360);
    if off <= span {
        return (lo + off).rem_euclid(360);
    }
    if off - span <= 360 - off {
        return hi.rem_euclid(360);
    }
    lo.rem_euclid(360)
}
